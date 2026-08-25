import { useState } from 'react';
import { useQuery } from '@tanstack/react-query';

function App() {
  const [showAll, setShowAll] = useState(false);

  const {
    data: posts,
    isLoading,
    isError,
    error,
  } = useQuery({
    queryKey: ['posts'],
    queryFn: async () => {
      const response = await fetch(
        'https://jsonplaceholder.typicode.com/posts'
      );

      if (!response.ok) {
        throw new Error('Не удалось загрузить посты');
      }

      return response.json();
    },
  });

  if (isLoading) {
    return <h2>Загрузка...</h2>;
  }

  if (isError) {
    return <h2>Ошибка: {error.message}</h2>;
  }

  const displayedPosts = showAll ? posts : posts.slice(0, 5);

  return (
    <div className="container">
      <h1>Список постов</h1>

      <button onClick={() => setShowAll(!showAll)}>
        {showAll ? 'Показать первые 5' : 'Показать все'}
      </button>

      <div className="posts">
        {displayedPosts.map((post) => (
          <article className="post" key={post.id}>
            <h2>{post.title}</h2>
            <p>{post.body.slice(0, 100)}</p>
          </article>
        ))}
      </div>
    </div>
  );
}

export default App;