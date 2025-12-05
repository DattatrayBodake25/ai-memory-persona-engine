// src/components/ChatInput.jsx
import React, { useState, useEffect } from "react";
import LoaderSpinner from "./LoaderSpinner";
import TypingIndicator from "./TypingIndicator";

const ChatInput = ({ onSend, isLoading, clearSignal }) => {
  const [message, setMessage] = useState("");

  // Clear the input when parent triggers clearSignal
  useEffect(() => {
    if (clearSignal) setMessage("");
  }, [clearSignal]);

  const handleSend = () => {
    if (!message.trim() || isLoading) return;
    onSend(message);
  };

  return (
    <div className="mb-6 p-5 bg-white rounded-xl shadow-md border">
      <label className="font-semibold text-gray-800 mb-2 block">
        Your Message
      </label>

      <textarea
        className="
          border border-gray-300 rounded-xl p-3 w-full h-28 resize-none
          focus:ring-2 focus:ring-blue-500 focus:border-blue-500 transition
          disabled:bg-gray-100 disabled:cursor-not-allowed
        "
        placeholder="Type something you'd tell an AI companion..."
        value={message}
        disabled={isLoading}
        onChange={(e) => setMessage(e.target.value)}
      />

      <button
        onClick={handleSend}
        disabled={isLoading}
        className={`
          mt-3 w-full py-2.5 rounded-lg font-medium shadow-sm transition
          ${isLoading
            ? "bg-gray-400 cursor-not-allowed text-white"
            : "bg-blue-600 hover:bg-blue-700 text-white"
          }
        `}
      >
        {isLoading ? "Sending..." : "Send Message"}
      </button>

      {isLoading && (
        <div className="mt-4 flex flex-col items-center space-y-2">
          <LoaderSpinner />
          <TypingIndicator />
        </div>
      )}
    </div>
  );
};

export default ChatInput;
