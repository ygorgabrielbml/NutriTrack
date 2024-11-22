import React, { useEffect, useState } from 'react';
import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '../ui/card';

type Vitamin = {
  label: string;
  color: string;
};

type VitaminsListProps = {
  vitaminsData: Vitamin[];
};

const VitaminsList = ({ vitaminsData }: VitaminsListProps) => {
  const [vitamins, setVitamins] = useState<Vitamin[] | []>([]);

  useEffect(() => {
    console.log(vitaminsData);

    setVitamins(vitaminsData);
  }, [vitaminsData]);

  return (
    <Card className="min-w-[400px]">
      <CardHeader>
        <CardTitle>Vitaminas</CardTitle>
        <CardDescription>
          Confira as vitaminas presente no seu alimento
        </CardDescription>
      </CardHeader>
      <CardContent>
        {vitamins &&
          vitamins.map((vitamin) => (
            <span className="flex items-center gap-x-2">
              <div
                className="size-2 rounded-full"
                style={{ backgroundColor: vitamin.color }}
              ></div>
              {vitamin.label}
            </span>
          ))}
      </CardContent>
    </Card>
  );
};

export default VitaminsList;
