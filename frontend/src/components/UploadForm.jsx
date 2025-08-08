// src/components/UploadForm.jsx
import React, { useState, useCallback } from 'react';
import axios from 'axios';
import { useDropzone } from 'react-dropzone';
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';

const UploadForm = () => {
  const [file, setFile] = useState(null);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles.length > 0) {
      setFile(acceptedFiles[0]);
    }
  }, []);

  const { getRootProps, getInputProps, open, isDragActive } = useDropzone({
    onDrop,
    noClick: true,
    noKeyboard: true,
    accept: {
      'application/pdf': ['.pdf'],
      'application/vnd.openxmlformats-officedocument.wordprocessingml.document': ['.docx'],
    },
    multiple: false,
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!file) return;

    setLoading(true);
    setResult(null);

    const formData = new FormData();
    formData.append("file", file);

    try {
      const res = await axios.post(`${import.meta.env.VITE_API_URL}/parse-cv/`, formData, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setResult(res.data);
      toast.success("CV parsed successfully!");
    } catch (err) {
      toast.error(err.response?.data?.detail || "Error parsing CV");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-8 bg-white shadow-2xl rounded-xl border border-gray-200">
      <h2 className="text-3xl font-bold text-gray-800 mb-6 text-center">
        Upload Your CV
      </h2>

      <form onSubmit={handleSubmit} className="space-y-6">
        <div
          {...getRootProps()}
          className={`border-2 border-dashed rounded-xl p-8 text-center transition-all duration-200 ${
            isDragActive
              ? 'border-blue-500 bg-blue-50'
              : 'border-gray-300 bg-gray-50 hover:border-blue-400'
          }`}
        >
          <input {...getInputProps()} />
          {file ? (
            <p className="text-green-600 font-medium">{file.name}</p>
          ) : (
            <>
              <p className="text-gray-600 font-medium">Drag & drop your CV here</p>
              <p className="text-gray-500 mt-2">or</p>
              <button
                type="button"
                onClick={open}
                className="mt-4 px-6 py-2 bg-blue-600 text-white rounded-lg shadow hover:bg-blue-700 transition"
              >
                Browse Files
              </button>
            </>
          )}
        </div>

        <button
          type="submit"
          disabled={!file || loading}
          className={`w-full py-3 px-4 text-lg font-semibold rounded-lg shadow transition ${
            loading
              ? 'bg-blue-300 cursor-not-allowed'
              : 'bg-blue-600 hover:bg-blue-700 text-white'
          }`}
        >
          {loading ? 'Parsing...' : 'Parse CV'}
        </button>
      </form>

      {result && (
        <div className="mt-8">
          <h3 className="text-lg font-semibold mb-3 text-gray-800">Parsed Result</h3>
          <pre className="bg-gray-100 p-4 rounded-lg text-sm overflow-x-auto whitespace-pre-wrap">
            {JSON.stringify(result, null, 2)}
          </pre>
        </div>
      )}

      <ToastContainer position="top-center" />
    </div>
  );
};

export default UploadForm;
