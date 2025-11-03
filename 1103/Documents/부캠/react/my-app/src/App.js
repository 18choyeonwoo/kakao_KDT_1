import logo from './logo.svg';
import './App.css';
import Header from './components/Header'
import MainBanner from './components/MainBanner';
import MainProduct from './components/MainProduct';
import Benefit from './components/Benefit';
import MainReward from './components/MainReward';

function App() {
  return (
   <div id="wrap">
      <Header />
      <MainBanner />
      <MainProduct />
      <Benefit />
      <MainReward />
    </div>
  );
}


export default App;