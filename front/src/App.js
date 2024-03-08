import './App.css';
import React, { useState } from 'react';

function App() {
  const [inputText, setInputText] = useState('');
  const [translatedText, setTranslatedText] = useState('');

  const handleInputChange = (event) => {
    setInputText(event.target.value);
  };

  const server_port = process.env.REACT_APP_SERVER_PORT;

  const handleTranslateClick = () => {

    fetch(`http://localhost:${server_port}/translate/invoke`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        "input": {
          "sentence": inputText
        }
      }),
    })
      .then(response => response.json())
      .then(data => setTranslatedText(data["output"]))
      .catch(error => console.error('Erro na chamada de API:', error));
  };

  return (
    <div className="App">
      <div id="general-container">
        <h1 id="page-title">Translator using LangChain 🦜🔗</h1>

        <div id="content-container">
          <div id="input-container">
            <input type="text" id="input" placeholder="Enter the text to be translated" value={inputText} onChange={handleInputChange}/>
            <button id="translate-btn" onClick={handleTranslateClick}>Translate</button>
          </div>
          <div id="translated-container">
            <textarea type="text" id="translated" placeholder="Digite o texto a ser traduzido" value={translatedText}/>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
