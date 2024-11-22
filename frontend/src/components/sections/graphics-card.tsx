import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import NutrientChart from './nutrientes-chart';

export function GraphicsCard() {
  return (
    <div className="mt-3">
      <NutrientChart />
      <div></div>

      <div></div>
    </div>
  );
}
