// src/components/TypingIndicator.jsx
import React, { useEffect, useState } from "react";

const TypingIndicator = () => {
  const [dots, setDots] = useState(".");

  useEffect(() => {
    const interval = setInterval(() => {
      setDots((prev) => (prev.length < 3 ? prev + "." : "."));
    }, 500);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="flex items-center space-x-2 py-2">
      <div className="w-3 h-3 bg-blue-400 rounded-full animate-pulse"></div>
      <p className="text-gray-600 font-medium text-sm">
        AI is thinking{dots}
      </p>
    </div>
  );
};

export default TypingIndicator;
