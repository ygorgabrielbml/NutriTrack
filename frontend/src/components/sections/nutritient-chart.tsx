'use client';

import { Bar, BarChart, CartesianGrid, XAxis } from 'recharts';

import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from '@/components/ui/card';
import {
  ChartConfig,
  ChartContainer,
  ChartTooltip,
  ChartTooltipContent,
} from '@/components/ui/chart';
import { useEffect, useState } from 'react';

const chartConfig = {
  desktop: {
    label: 'Nutrientes',
    color: 'hsl(var(--chart-1))',
  },
} satisfies ChartConfig;

type NutrientChartProps = {
  chartData: any;
};

export default function NutrientChart({ chartData }: NutrientChartProps) {
  const [data, setData] = useState(chartData || undefined);

  useEffect(() => {
    setData(chartData);
  }, [chartData]);

  return (
    <Card className="w-[400px]">
      <CardHeader>
        <CardTitle>Nutrientes</CardTitle>
        <CardDescription>Nutrientes presentes no alimento</CardDescription>
      </CardHeader>
      <CardContent>
        <ChartContainer config={chartConfig}>
          <BarChart accessibilityLayer data={data}>
            <CartesianGrid vertical={false} />
            <XAxis
              dataKey="name"
              tickLine={false}
              tickMargin={1}
              axisLine={false}
              tickFormatter={(value) => value.slice(0, 3)}
            />
            <ChartTooltip
              cursor={false}
              content={<ChartTooltipContent hideLabel />}
            />
            <Bar dataKey="amt" fill="var(--color-desktop)" radius={8} />
          </BarChart>
        </ChartContainer>
      </CardContent>
      <CardFooter></CardFooter>
    </Card>
  );
}
