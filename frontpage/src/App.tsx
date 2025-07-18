import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ArticleView from "./pages/ArticleView";
import HomePage from "./pages/HomePage"


function App() {

  return (
    <>
      <Router>
        <header className="flex flex-col items-center justify-center">
          <h1 className="mb-10 select-none font-bold text-5xl"><span className="bg-[url('/images/rugged-paper.png')] text-shadow-lg bg-cover bg-no-repeat bg-center bg-clip-text text-transparent relative after:content-[attr(data-text)] after:absolute after:left-0 after:text-transparent after:bg-clip-text after:text-shadow-lg after:z-[-1]" data-text="Front">Front</span><span className="relative text-white top-4 z-10 before:absolute before:right-[-0.5rem] before:bottom-[-0.25rem] before:w-[120%] before:h-[90%] before:bg-[url('/images/rugged-paper.png')] before:bg-cover before:bg-no-repeat before:bg-center before:z-[-1] before:[clip-path:polygon(10%_0%,100%_0%,100%_100%,0%_100%)] after:content-[attr(data-text)] after:absolute after:left-0 after:top-2 after:text-transparent after:bg-clip-text after:text-shadow-lg after:z-[-1]" data-text="Page">Page</span></h1>
          <div className="w-full h-[1px] bg-black"></div>
          <h2 className="font-medium text-xl">Your trustworthy news compiler ♡</h2>
        </header>
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/article/:id" element={<ArticleView />} />
        </Routes>
    </Router>
    </>
  )
}

export default App
