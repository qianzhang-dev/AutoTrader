import React from 'react';
import logo from '../resources/logo.svg';
import '../css/App.css';
import { MarketQuickGlance } from './components/tradeViewWidgets/MarketQuickGlance';
import { AutoTraderMainLayout } from './layouts/AutoTraderMainLayout';

function App() {


  return (
    <div className="App">
      <AutoTraderMainLayout />
    </div>
  );
}

export default App;
