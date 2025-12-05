// src/components/Toast.jsx
import React, { useEffect } from "react";

const Toast = ({ message, type = "info", onClose }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, 2500);

    return () => clearTimeout(timer);
  }, [onClose]);

  const bgColors = {
    info: "bg-blue-500",
    success: "bg-green-500",
    error: "bg-red-500",
    warning: "bg-yellow-500 text-black"
  };

  return (
    <div className="fixed top-5 right-5 z-50">
      <div
        className={`
          ${bgColors[type]} 
          text-white px-4 py-2 rounded-lg shadow-lg animate-fadeIn
        `}
      >
        {message}
      </div>
    </div>
  );
};

export default Toast;
