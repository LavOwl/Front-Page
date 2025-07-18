import { Link } from "react-router-dom"
import { type Article } from "../types/Article"


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
                <Link to={"/article/" + article._id} className="absolute right-0 top-1/2 transform translate-y-[-50%] p-6 rounded-full hover:bg-gray-400 cursor-pointer"><span className="absolute left-1/2 top-1/2 p-2 w-0 h-0 aspect-square border-l border-b rotate-225 border-black transform translate-[-50%] before:content-[''] before:h-[0.5px] before:w-6 before:bg-black before:absolute before:origin-center before:transform before:left-[-0.233525rem] before:top-1/2 before:translate-y-[-50%] before:rotate-135"></span></Link>
            </div>
        </>
    )
}

export default ArticlePreview