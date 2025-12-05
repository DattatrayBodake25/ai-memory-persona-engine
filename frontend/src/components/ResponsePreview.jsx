// src/components/ResponsePreview.jsx
import React from "react";

const ResponsePreview = ({ response }) => {
  if (!response) return null;

  return (
    <div className="mt-6">

      {/* USER MESSAGE BOX */}
      <div className="bg-white rounded-xl shadow-md border p-5 mb-6">
        <h3 className="font-semibold text-gray-700 mb-2">Your Message</h3>
        <p className="p-3 bg-gray-50 rounded-lg text-gray-900 leading-relaxed border">
          {response.user_message}
        </p>
      </div>

      {/* SECTION TITLE */}
      <h2 className="text-xl font-bold mb-4 text-gray-900">AI Responses</h2>

      {/* HORIZONTAL CARDS */}
      <div className="flex flex-col md:flex-row gap-4">

        {/* Neutral Response */}
        <div className="flex-1 bg-white rounded-xl shadow-md border p-5">
          <h3 className="font-semibold text-gray-700 mb-2">Neutral Response</h3>
          <p className="p-3 bg-gray-100 rounded-lg text-gray-900 leading-relaxed shadow-sm">
            {response.neutral_response}
          </p>
        </div>

        {/* Persona Styled Response */}
        <div className="flex-1 bg-white rounded-xl shadow-md border p-5">
          <h3 className="font-semibold text-gray-700 mb-2">Persona Styled Response</h3>
          <p className="p-3 bg-blue-50 rounded-lg text-gray-900 leading-relaxed shadow-sm border border-blue-200">
            {response.styled_response}
          </p>
        </div>

      </div>
    </div>
  );
};

export default ResponsePreview;
