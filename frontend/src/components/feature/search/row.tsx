import { cn } from '@/lib/utils';
import { Heart } from 'lucide-react';
import React, { HTMLAttributes, useState } from 'react';

type RowResultProps = {
  name: string;
  selectedFood: boolean;
} & HTMLAttributes<HTMLDivElement>;

const RowResult = ({ name, selectedFood, ...props }: RowResultProps) => {
  const [favorite, setFavorite] = useState<boolean>(false);

  function handleFavorite(event: React.MouseEvent<SVGElement>) {
    setFavorite(!favorite);
    event.stopPropagation(); // Prevent triggering the parent onClick
  }

  return (
    <div
      className={cn(
        'flex rounded bg-gray-50 px-3 py-2 justify-between cursor-pointer',
        selectedFood && 'bg-green-50',
      )}
      {...props}
    >
      {name}
      <div className="flex items-center gap-x-3">
        <Heart
          size={16}
          onClick={handleFavorite}
          fill={favorite ? 'red' : 'none'}
          className="cursor-pointer"
        />
      </div>
    </div>
  );
};

export default RowResult;
