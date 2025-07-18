import { useEffect, useState } from "react"
import { type Article } from "./types/Article"
import ArticlePreview from "./components/ArticlePreview"


function App() {
  const [articles, setArticles] = useState<Article[]>([])

  /*var articles:Article[] = [{url:"https://www.pagina12.com.ar/838971-el-jp-morgan-y-los-campeones-corren-a-caputo", title:"Título importante", author:["Juan", "Leticia"], tags:["Frfr"], date:"25/6/25"},
                            {url:"https://www.pagina12.com.ar/838971-el-jp-morgan-y-los-campeones-corren-a-caputo", title:"Título importante", author:["Robert", "Manuel"], tags:["Real no fake"], date:"25/6/25"},
                            {url:"https://www.pagina12.com.ar/838971-el-jp-morgan-y-los-campeones-corren-a-caputo", title:"Título importante", author:["Silvia"], tags:["El facismo sigue acercandose"], date:"25/6/25"},
                            {url:"https://www.pagina12.com.ar/838971-el-jp-morgan-y-los-campeones-corren-a-caputo", title:"Título importante", author:["Pedro"], tags:["Increible"], date:"25/6/25"},
                            {url:"https://www.pagina12.com.ar/838971-el-jp-morgan-y-los-campeones-corren-a-caputo", title:"Título importante", author:["Agata"], tags:["NotATag"], date:"25/6/25"},
                            {url:"https://www.pagina12.com.ar/838971-el-jp-morgan-y-los-campeones-corren-a-caputo", title:"Título importante", author:["Angela"], tags:["LetMeOut"], date:"25/6/25"},
                           ]*/

  useEffect(() => {
    fetch("http://localhost:8000/articles")
      .then((res) => res.json())
      .then((data) => setArticles(data))
      .catch((err) => console.error("Error fetching articles:", err))
  }, [])

  return (
    <>
      
      <main className="flex flex-col items-center justify-center">
        <h1 className="mb-10 select-none font-bold text-5xl"><span className="bg-[url('/images/rugged-paper.png')] text-shadow-lg bg-cover bg-no-repeat bg-center bg-clip-text text-transparent relative after:content-[attr(data-text)] after:absolute after:left-0 after:text-transparent after:bg-clip-text after:text-shadow-lg after:z-[-1]" data-text="Front">Front</span><span className="relative text-white top-4 z-10 before:absolute before:right-[-0.5rem] before:bottom-[-0.25rem] before:w-[120%] before:h-[90%] before:bg-[url('/images/rugged-paper.png')] before:bg-cover before:bg-no-repeat before:bg-center before:z-[-1] before:[clip-path:polygon(10%_0%,100%_0%,100%_100%,0%_100%)] after:content-[attr(data-text)] after:absolute after:left-0 after:top-2 after:text-transparent after:bg-clip-text after:text-shadow-lg after:z-[-1]" data-text="Page">Page</span></h1>
        <div className="w-full h-[1px] bg-black"></div>
        <h2 className="font-medium text-xl">Your trustworthy news compiler ♡</h2>
        <div className="relative">
          <input className="outline-transparent border-1 rounded-3xl pl-4 pr-12 py-1" placeholder="Search" type="text"/>
          <span className="cursor-pointer w-auto h-full border-l-1 absolute right-1 top-1/2 transform translate-y-[-50%] flex items-center justify-center">
            <img src="/icons/magnifying-glass.svg" className="h-3/5 px-2"/>
          </span>
        </div>

        <ul className="w-full max-w-xl mt-4">
        {articles.map((article, idx) => (
          <li key={idx} className="border-b py-2">
            <ArticlePreview article={article}/>
          </li>
        ))}
      </ul>
      </main>
    </>
  )
}

export default App
