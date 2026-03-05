import { useState } from "react";

function App(){

const [notes,setNotes] = useState("")
const [quiz,setQuiz] = useState("")

async function generateQuiz(){

const res = await fetch("http://localhost:8000/quiz",{
method:"POST",
headers:{ "Content-Type":"application/json"},
body:JSON.stringify({text:notes})
})

const data = await res.json()

setQuiz(data.quiz)

}

return(

<div>

<h1>AP AI Tutor</h1>

<textarea
onChange={(e)=>setNotes(e.target.value)}
placeholder="Paste notes here"
/>

<button onClick={generateQuiz}>
Generate Quiz
</button>

<pre>{quiz}</pre>

</div>

)

}

export default App
