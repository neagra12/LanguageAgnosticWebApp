import React from "react";

interface Props {
  id: string;
  files: string[]; // ✅ required prop now
}

const VisualizationDisplay: React.FC<Props> = ({ id, files }) => {
  const baseUrl = `http://localhost:8000/outputs/${id}`;
  console.log("📦 files received:", files);



  return (
    <div className="mt-6 text-center">
      <h2 className="text-xl font-semibold mb-4">Generated Visualization</h2>
      
      <div className="space-y-4">
      {files.includes("plot.png") && (
  <>
    <p className="text-sm text-gray-500">🖼️ Image Path: {`${baseUrl}/plot.png`}</p>
    <img
      src={`${baseUrl}/plot.png`}
      alt="Static Plot"
      className="mx-auto max-w-full border rounded shadow"
    />
  </>
)}

        {files.includes("plot.html") && (
  <>
    <p className="text-sm text-gray-500">➡️ HTML Path: {`${baseUrl}/plot.html`}</p>
    <a href={`${baseUrl}/plot.html`} target="_blank" className="text-blue-500 underline text-sm">
  Open plot.html in a new tab ↗
</a>

    <iframe
  src={`${baseUrl}/plot.html`}
  title="Interactive Plot"
  className="w-full border border-gray-300 rounded shadow"
  style={{
    height: "800px",
    backgroundColor: "white",
    display: "block",
  }}
  allow="fullscreen" // ✅ optional, but helpful for 3D plots
  sandbox="allow-same-origin allow-scripts allow-popups" // ✅ important for JS-based HTML
/>

  </>
)}

      </div>
    </div>
  );
};

export default VisualizationDisplay;
