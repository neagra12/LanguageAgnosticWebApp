import React from "react";

interface Props {
  code: string;
  setCode: (code: string) => void;
}

const CodeEditor: React.FC<Props> = ({ code, setCode }) => {
  return (
    <div>
      <label className="font-semibold block mb-2">Enter Code:</label>
      <textarea
        className="w-full border rounded p-2 font-mono text-sm"
        rows={10}
        value={code}
        onChange={(e) => setCode(e.target.value)}
        placeholder="Write your Python or R code here..."
      />
    </div>
  );
};

export default CodeEditor;
