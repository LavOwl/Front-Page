import { Link } from "react-router-dom"
import { type Article } from "../types/Article"
import Arrow from "./Arrow"


type ArticlePreviewProps = {
  article: Article
}

function ArticlePreview({ article } : ArticlePreviewProps) {

    return (
        <>
            <div className="relative">
                <p className="font-semibold">{article.title}</p>
                <a href={article.url} className="border-1 rounded-2xl max-w-[35%] block text-nowrap overflow-hidden text-ellipsis whitespace-nowrap px-1 py-0.5 text-sm bg-gray-200 text-gray-700 hover:bg-gray-300 hover:text-gray-800"><abbr className="no-underline" title={article.url}>{article.url}</abbr></a>
                <p className="text-sm text-gray-500">{article.author?.join(", ")}</p>
                <p className="text-xs text-gray-400">{article.date}</p>
                <Link to={"/article/" + article._id} className="absolute right-0 top-1/2 transform translate-y-[-50%] p-5 rounded-full hover:bg-gray-400/50 z-0 cursor-pointer"><Arrow angle={225}/></Link>
            </div>
        </>
    )
}

export default ArticlePreview