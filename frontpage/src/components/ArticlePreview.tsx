import { type Article } from "../types/Article"

type ArticlePreviewProps = {
  article: Article
}

function ArticlePreview({ article } : ArticlePreviewProps) {

    return (
        <>
            <p className="font-semibold">{article.title}</p>
            <a href={article.url} className="border-1 rounded-2xl max-w-[35%] block text-nowrap overflow-hidden text-ellipsis whitespace-nowrap px-1 py-0.5 text-sm bg-gray-200 text-gray-700 hover:bg-gray-300 hover:text-gray-800"><abbr className="no-underline" title={article.url}>{article.url}</abbr></a>
            <p className="text-sm text-gray-500">{article.author?.join(", ")}</p>
            <p className="text-xs text-gray-400">{article.date}</p>
        </>
    )
}

export default ArticlePreview