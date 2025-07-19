import { useParams, Link } from 'react-router-dom';
import { useEffect, useState } from "react";
import { type Article } from "../types/Article";
import Arrow from "../components/Arrow"

export default function ArticleView() {

    const { id } = useParams();

    const [article, setArticle] = useState<Article>()
    
    useEffect(() => {
        fetch("http://localhost:8000/articles/" + id)
        .then((res) => res.json())
        .then((data) => setArticle(data))
        .catch((err) => console.error("Error fetching articles:", err))
    }, [])

    return (
        <>
            <div className="w-full relative">
            <Link to={"/"} className="absolute left-3 top-0 p-5 rounded-full hover:bg-gray-400/50 z-0 cursor-pointer"><Arrow angle={45}/></Link>
                <main className="flex flex-col w-1/2 justify-center m-auto">
                    <h1 className="uppercase text-2xl font-semibold">{article?.title} <span className="capitalize float-right font-light text-xl"><br/>• Por {article?.newspaper}</span></h1>
                    <br/>
                    <p className="font-light text-lg/relaxed">
                        {article?.body.split('\n').map((paragraph, index) => (
                            <span key={index}>
                            {paragraph}
                            <br />
                            <br />
                            </span>
                        ))}
                    </p>
                </main>
            </div>
        </>
    );
}