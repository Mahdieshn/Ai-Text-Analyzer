import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const analyzeText = async () => {
    setLoading(true);
    try {
      const response = await axios.post('http://localhost:8000/analyze', { content: text });
      setResult(response.data.data);
    } catch (error) {
      alert("خطا در ارتباط با سرور!");
    }
    setLoading(false);
  };

  return (
    <div className="container">
      <h1>AI Text Analyzer</h1>
      <textarea 
        placeholder="Enter your text here..." 
        value={text} 
        onChange={(e) => setText(e.target.value)}
      />
      <button onClick={analyzeText} disabled={loading}>
        {loading ? 'Analyzing...' : 'Analyze Now'}
      </button>

      {result && (
        <div className="result">
          <h3>Analysis Results:</h3>
          <p><strong>Words:</strong> {result.word_count}</p>
          <p><strong>Sentences:</strong> {result.sentence_count}</p>
          <h4>Entities Found:</h4>
          <ul>
            {result.entities.map((ent, i) => (
              <li key={i}>{ent.text} <span className="label">({ent.label})</span></li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;