import logo from './logo.svg';
import './App.css';
import Header from './components/Header'
import MainBanner from './components/MainBanner';
import MainProduct from './components/MainProduct';

function App() {
  return (
   <div id="wrap">
      <Header />
      <MainBanner />
      <MainProduct />
    </div>
  );
}


export default App;