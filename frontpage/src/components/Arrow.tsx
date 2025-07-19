export default function Arrow({angle}: {angle:number}){
    return (
        <span style={{ transform: `rotate(${angle}deg)`}} className="absolute left-1/2 top-1/2 p-2 w-0 h-0 aspect-square border-l border-b border-black transform translate-[-50%] before:content-[''] before:h-[0.5px] before:w-6 before:bg-black before:absolute before:origin-center before:transform before:left-[-0.233525rem] before:top-1/2 before:translate-y-[-50%] before:rotate-135"></span>
    )
}