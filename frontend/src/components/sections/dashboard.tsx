import {
  Card,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import NutrientChart from './nutritient-chart';
import { Calendar } from '../ui/calendar';
import { useEffect, useState } from 'react';
import { Input } from '../ui/input';
import { foods as mockFoods } from 'constants/foods';
import RowResult from '../feature/search/row';
import VitaminsList from './vitamins-list';
import IngradientList from './ingredient-list';

export default function Dashboard() {
  const [date, setDate] = useState<Date | undefined>(undefined);
  const [data, setData] = useState<any | undefined>(undefined);
  const [search, setSearch] = useState<string>('');
  const [foods, setFoods] = useState(mockFoods);
  const [selectedFood, setSelectedFood] = useState<number | null>(null);
  const [nutrientData, setNutrientData] = useState<any>(null);
  const [vitaminsData, setVitaminsData] = useState<any>(null);
  const [ingredientsData, setIngredientsData] = useState<any>(null);

  useEffect(() => {
    if (selectedFood) {
      const selectedFoodData = mockFoods.find(
        (food) => selectedFood! === food.id,
      );

      if (selectedFoodData) {
        setNutrientData(selectedFoodData.nutrients);
        setVitaminsData(selectedFoodData.vitamins);
        setIngredientsData(selectedFoodData.ingredients);
      }
    }
  }, [selectedFood]);

  const onSearchChange = (event: any) => {
    const value = event.target.value;
    setSearch(value);

    if (value) {
      const filteredArr = foods.filter((food) => {
        return food.name.toLowerCase().includes(value);
      });

      setFoods(filteredArr);
      return;
    }

    setFoods(mockFoods);
  };

  return (
    <div className="px-12 mt-5 ml-16">
      <Input
        placeholder="Pesquisa de alimento"
        className="mb-3"
        value={search}
        onChange={onSearchChange}
      />
      <div className="flex">
        <Card className="bg-white text-black w-[900px]">
          <CardHeader>
            <CardTitle>Comidas</CardTitle>
            <CardDescription>
              Explore nosso catalogo de alimentos
            </CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex flex-col overflow-y-auto gap-y-1 max-h-80 ">
              {foods.map((food) => (
                <RowResult
                  name={food.name}
                  key={food.id}
                  onClick={() => setSelectedFood(food.id)}
                  selectedFood={selectedFood === food.id}
                />
              ))}
            </div>
          </CardContent>
        </Card>
        <Card className="ml-3">
          <CardHeader className="text-2xl font-bold">Calendário</CardHeader>
          <CardContent>
            <Calendar
              mode="single"
              selected={date}
              onSelect={setDate}
              className="h-full w-full flex"
              classNames={{
                months:
                  'flex flex-col sm:flex-row space-y-4 sm:space-x-4 sm:space-y-0 flex-1',
                month: 'space-y-4 w-full flex flex-col',
                table: 'w-full h-full border-collapse space-y-1',
                head_row: '',
                row: 'w-full mt-2',
              }}
            />
          </CardContent>
        </Card>
      </div>
      <div className="flex space-x-3 mt-3">
        <NutrientChart chartData={nutrientData} />
        <VitaminsList vitaminsData={vitaminsData} />
        <IngradientList ingredients={ingredientsData} />
      </div>
    </div>
  );
}
