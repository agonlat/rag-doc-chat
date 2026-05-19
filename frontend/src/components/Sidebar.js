import React from "react";
import { useState } from "react";
import axios from "axios"

function Sidebar() {

    const [files,setFiles] = useState([])
    console.log(files)

    async function handleUpload() {
const form = new FormData()

for (const file of files) {
form.append("files",file)
}
const response = await axios.post("http://localhost:8000/api/documents/upload", form)
}





    return (
        <div>
            <h2>Documents</h2>
            <input type = "file" multiple accept="application/pdf" onChange={(e)=>setFiles(e.target.files)}></input>
            <button onClick={()=>handleUpload()}></button>
        </div>
    )
}



export default Sidebar