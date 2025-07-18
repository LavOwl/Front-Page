import { useEffect, useState } from "react"
import { type Article } from "../types/Article"
import ArticlePreview from "../components/ArticlePreview"

export default function HomePage() {
    
    const [articles, setArticles] = useState<Article[]>([])

    useEffect(() => {
        fetch("http://localhost:8000/articles")
        .then((res) => res.json())
        .then((data) => setArticles(data))
        .catch((err) => console.error("Error fetching articles:", err))
    }, [])

    return (

    <main className="flex flex-col items-center justify-center">
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
    );
}