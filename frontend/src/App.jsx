// src/App.jsx
import React, { useState, useEffect } from "react";

import PersonalitySelector from "./components/PersonalitySelector";
import ChatInput from "./components/ChatInput";
import MemoryView from "./components/MemoryView";
import ResponsePreview from "./components/ResponsePreview";
import Toast from "./components/Toast";

import { getAllMemory, transformPersona } from "./services/api";

const App = () => {
  const [memory, setMemory] = useState(null);
  const [persona, setPersona] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const [clearInput, setClearInput] = useState(false);
  const [toast, setToast] = useState(null);

  // Load memory at startup
  useEffect(() => {
    async function loadMemory() {
      const mem = await getAllMemory();
      setMemory(mem);
    }
    loadMemory();
  }, []);

  const showToast = (message, type = "info") => {
    setToast({ message, type });
  };

  // When user sends a message → neutral + persona responses returned
  const handleSend = async (message) => {
    if (!persona) {
      return showToast("Please select a persona before sending!", "warning");
    }

    if (!message.trim()) return;

    setLoading(true);

    try {
      const ai = await transformPersona(message, persona);

      // include the user's original message
      setResponse({
        ...ai,
        user_message: message,
      });
    } catch (err) {
      showToast("Error generating AI response. Try again!", "error");
    }

    setLoading(false);

    // Clear input after send
    setClearInput(true);
    setTimeout(() => setClearInput(false), 80);
  };

  return (
    <div className="min-h-screen bg-gray-100 py-10">
      <div className="max-w-3xl mx-auto px-4">

        <h1 className="text-3xl font-bold mb-8 text-center text-gray-900">
          Gupshupp AI Assignment Demo
        </h1>

        {/* Toast */}
        {toast && (
          <Toast
            message={toast.message}
            type={toast.type}
            onClose={() => setToast(null)}
          />
        )}

        {/* Memory Section */}
        <MemoryView memory={memory} />

        {/* Persona Selector */}
        <PersonalitySelector persona={persona} setPersona={setPersona} />

        {/* AI Response Section */}
        <ResponsePreview response={response} />

        {/* Input Box */}
        <ChatInput
          onSend={handleSend}
          isLoading={loading}
          clearSignal={clearInput}
        />

      </div>
    </div>
  );
};

export default App;
