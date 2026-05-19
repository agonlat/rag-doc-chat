import React from 'react';
import { useState } from 'react';
import Sidebar from './components/Sidebar';

function App() {
  const [name, setName] = useState("Max")
  
  return (
     <Sidebar />
  )
}

export default App;