import { MemoryRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import 'tailwindcss/tailwind.css';
import { SidebarProvider, SidebarTrigger } from '@/components/ui/sidebar';
import { SideBarMenu } from '@/components/sections/sidebar-menu';
import { Search } from '@/components/sections/search-bar';
import { ReactNode } from 'react';
import Dashboard from '@/components/sections/dashboard';

export default function App({ children }: { children: ReactNode }) {
  return (
    <SidebarProvider>
      <SideBarMenu />
      <main>
        <SidebarTrigger />
        <Dashboard />
      </main>
    </SidebarProvider>
  );
}
