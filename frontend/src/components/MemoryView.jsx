// src/components/MemoryView.jsx
import React, { useState } from "react";
import { ChevronDown, ChevronUp } from "lucide-react";
import { Heart, Star, Bookmark } from "lucide-react";

const Section = ({ title, icon, children }) => {
  const [open, setOpen] = useState(true);

  return (
    <div className="border rounded-lg bg-white shadow-sm mb-3">
      <button
        onClick={() => setOpen(!open)}
        className="w-full flex justify-between items-center p-3 text-left 
          font-semibold text-gray-800 hover:bg-gray-50 transition"
      >
        <div className="flex items-center gap-2">
          {icon}
          {title}
        </div>

        {open ? <ChevronUp size={18} /> : <ChevronDown size={18} />}
      </button>

      {open && (
        <div className="px-4 pb-3 text-gray-700 animate-fadeIn">
          {children}
        </div>
      )}
    </div>
  );
};

const MemoryView = ({ memory }) => {
  if (!memory) return null;

  return (
    <div className="p-5 bg-gray-50 rounded-xl shadow-md mb-6 border">
      <h2 className="text-xl font-bold text-gray-900 mb-4">
        Extracted Memory
      </h2>

      {/* User Preferences */}
      <Section 
        title="User Preferences" 
        icon={<Star size={18} className="text-yellow-500" />}
      >
        <ul className="list-disc ml-6">
          {memory.user_preferences?.map((p, idx) => (
            <li key={idx} className="py-1">
              <span className="font-semibold capitalize">{p.topic}</span>: {p.preference}
            </li>
          ))}
        </ul>
      </Section>

      {/* Emotional Patterns */}
      <Section 
        title="Emotional Patterns" 
        icon={<Heart size={18} className="text-red-500" />}
      >
        <ul className="list-disc ml-6">
          {memory.emotional_patterns?.map((e, idx) => (
            <li key={idx} className="py-1">{e.pattern}</li>
          ))}
        </ul>
      </Section>

      {/* Factual Memories */}
      <Section 
        title="Factual Memories" 
        icon={<Bookmark size={18} className="text-blue-500" />}
      >
        <ul className="list-disc ml-6">
          {memory.factual_memories?.map((f, idx) => (
            <li key={idx} className="py-1">{f.fact}</li>
          ))}
        </ul>
      </Section>
    </div>
  );
};

export default MemoryView;
