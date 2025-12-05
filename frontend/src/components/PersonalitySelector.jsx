import React from "react";

const PersonalitySelector = ({ persona, setPersona }) => {
  return (
    <div className="mb-6 p-5 bg-white rounded-xl shadow-md border">
      <label className="font-semibold text-gray-800 mb-2 block">Choose AI Persona</label>

      <select
        value={persona}
        onChange={(e) => setPersona(e.target.value)}
        className="p-3 border border-gray-300 rounded-lg w-full bg-gray-50 focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition"
      >
        <option value="">-- Select Persona Style --</option>
        <option value="calm mentor">Calm Mentor</option>
        <option value="witty friend">Witty Friend</option>
        <option value="therapist-style">Therapist Style</option>
        <option value="strict coach">Strict Coach</option>
        <option value="playful buddy">Playful Buddy</option>
      </select>
    </div>
  );
};

export default PersonalitySelector;
