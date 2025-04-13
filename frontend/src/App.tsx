import React, { useState } from 'react';
import LanguageSelector from './components/LanguageSelector';
import CodeEditor from './components/CodeEditor';
import VisualizationDisplay from './components/VisualizationDisplay';

function App() {
  const [language, setLanguage] = useState("python");
  const [code, setCode] = useState("");
  const [outputId, setOutputId] = useState("");
  const [outputFiles, setOutputFiles] = useState<string[]>([]);  // Tracks returned filenames

  const handleGenerate = async () => {
    try {
      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ language, code }),
      });

      if (!res.ok) {
        throw new Error("Failed to generate visualization");
      }

      const data = await res.json();
      console.log("📥 API response:", data);  // <-- this will log the received id and files

      setOutputId(data.id);
      setOutputFiles(data.files);  // ✅ Update the files state
    } catch (err) {
      console.error("Generation error:", err);
      alert("Something went wrong while generating the visualization.");
    }
  };

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      <h1 className="text-3xl font-bold mb-6 text-center text-indigo-600">
        Language-Agnostic Visualizer
      </h1>
      <div className="max-w-4xl mx-auto bg-white shadow-md rounded-xl p-6 space-y-4">
        <LanguageSelector language={language} setLanguage={setLanguage} />
        <CodeEditor code={code} setCode={setCode} />
        
        <button
          className="bg-indigo-600 text-white px-4 py-2 rounded hover:bg-indigo-700 transition"
          onClick={handleGenerate}
        >
          Generate Visualization
        </button>

        {outputId && <VisualizationDisplay id={outputId} files={outputFiles} />}
      </div>
    </div>
  );
}

export default App;
