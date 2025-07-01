// src/components/UploadForm.jsx
import React, { useState } from 'react';
import axios from 'axios';
import { UploadCloud, Loader2 } from 'lucide-react'; // add lucide-react icons

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    setError("");
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/parse-cv/`, formData, {
        headers: {
          "Content-Type": "multipart/form-data"
        }
      });
      setResult(res.data);
    } catch (err) {
      console.error("Full error:", err);
      setError(err.response?.data?.detail || "Error parsing CV");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-xl mx-auto bg-white p-6 rounded-2xl shadow-md border border-gray-200">
      <h2 className="text-2xl font-semibold mb-6 text-gray-800 flex items-center gap-2">
        <UploadCloud className="w-6 h-6 text-blue-500" />
        Upload Your CV
      </h2>

      <form onSubmit={handleSubmit} className="space-y-4">
        <label className="block">
          <span className="text-gray-700">Choose a PDF file</span>
          <input
            type="file"
            accept=".pdf"
            onChange={e => {
              const selectedFile = e.target.files[0];
              if (selectedFile && selectedFile.type !== "application/pdf") {
                setError("Only PDF files are supported.");
                setFile(null);
                e.target.value = "";
                return;
              }
              setError("");
              setFile(selectedFile);
            }}
            className="mt-1 block w-full text-sm text-gray-500
                      file:mr-4 file:py-2 file:px-4
                      file:rounded-md file:border-0
                      file:text-sm file:font-semibold
                      file:bg-blue-50 file:text-blue-700
                      hover:file:bg-blue-100"
          />
        </label>

        <button
          type="submit"
          disabled={!file || loading}
          className="flex items-center justify-center gap-2 w-full px-4 py-2 bg-blue-600 text-white font-medium rounded-md hover:bg-blue-700 transition disabled:bg-blue-300"
        >
          {loading ? (
            <>
              <Loader2 className="animate-spin w-5 h-5" />
              Parsing...
            </>
          ) : (
            "Parse CV"
          )}
        </button>
      </form>

      {error && <div className="mt-4 text-red-600">{error}</div>}

      {result && (
        <div className="mt-6">
          <h3 className="font-semibold text-gray-800 mb-2">Parsed Result</h3>
          <pre className="bg-gray-100 rounded-md p-4 text-sm overflow-x-auto max-h-96">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}
    </div>
  );
};

export default UploadForm;