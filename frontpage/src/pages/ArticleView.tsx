import { useParams } from 'react-router-dom';
import { useEffect, useState } from "react";
import { type Article } from "../types/Article";

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
        <div>
            <h1>{article?.title}</h1>
            <p>{article?.body}</p>
        </div>
    );
}