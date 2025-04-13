import React from "react";

interface Props {
  language: string;
  setLanguage: (lang: string) => void;
}

const LanguageSelector: React.FC<Props> = ({ language, setLanguage }) => {
  return (
    <div className="flex gap-4 items-center">
      <label className="font-semibold">Select Language:</label>
      <select
        value={language}
        onChange={(e) => setLanguage(e.target.value)}
        className="border rounded px-2 py-1"
      >
        <option value="python">Python</option>
        <option value="r">R</option>
      </select>
    </div>
  );
};

export default LanguageSelector;
