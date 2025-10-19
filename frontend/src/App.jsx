import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Toaster } from 'react-hot-toast';
import Layout from './components/Layout/Layout';
import Dashboard from './pages/Dashboard';
import SuppliersPage from './pages/SuppliersPage';
import ComponentsPage from './pages/ComponentsPage';
import WarehousesPage from './pages/WarehousesPage';
import OrdersPage from './pages/OrdersPage';
import StorekeepersPage from './pages/StorekeepersPage';
import SuppliesPage from './pages/SuppliesPage';

function App() {
  return (
    <BrowserRouter>
      <Toaster />
      <Routes>
        <Route path="/" element={<Layout />}>
          <Route index element={<Dashboard />} />
          <Route path="suppliers" element={<SuppliersPage />} />
          <Route path="components" element={<ComponentsPage />} />
          <Route path="warehouses" element={<WarehousesPage />} />
          <Route path="orders" element={<OrdersPage />} />
          <Route path="storekeepers" element={<StorekeepersPage />} />
          <Route path="supplies" element={<SuppliesPage />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
