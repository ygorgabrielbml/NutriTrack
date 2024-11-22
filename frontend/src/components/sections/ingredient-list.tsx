import React from 'react';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '../ui/card';
import RowResult from '../feature/search/row';

type Ingredient = {
  name: string;
  qnt: string;
};

type IngradientListProps = {
  ingredients: Ingredient[];
};

const IngradientList = ({ ingredients }: IngradientListProps) => {
  return (
    <Card className="bg-white text-black w-[630px]">
      <CardHeader>
        <CardTitle>Ingredientes</CardTitle>
        <CardDescription>Ingredientes do alimento selecionado</CardDescription>
      </CardHeader>
      <CardContent>
        {ingredients &&
          ingredients.map((ingredient) => (
            <div className="flex items-center justify-between">
              <span>{ingredient.name}</span>
              <span>{ingredient.qnt}</span>
            </div>
          ))}
      </CardContent>
    </Card>
  );
};

export default IngradientList;
