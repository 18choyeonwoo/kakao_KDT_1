// 큰 이미지 슬라이드 (item-big) + 썸네일 리스트 (item-thumb) 
// + 페이지네이션 (item-page) + 컴포넌트: MainBanner.jsx
import './MainBanner.css';


export default function MainBanner() {
  return (
    <div className="main-banner">
        {/* 큰 배너 이미지 */}
      <div className="item-big">
        <ul>
          <li>
            <a href="https://www.outback.co.kr/menu/productList.do?cateIdx=52&menuIdx=43" className="btn-cell">
              <img src="/20250618153158214175.png" alt="블랙라벨 쥬라기월드" />
            </a>
          </li>
          <li>
            <a href="/menu/productView.do?cateIdx=53&pdtIdx=10319&menuIdx=43" className="btn-cell">
              <img src="/20250616093330346112.png" alt="Sizzling Bone-In Steak" />
            </a>
          </li>
          <li>
            <a href="https://www.outback.co.kr/menu/productList.do?cateIdx=24&menuIdx=43" className="btn-cell">
              <img src="/20250613154912471100.png" alt="Lunch set" />
            </a>
          </li>
          <li>
            <a href="https://www.outback.co.kr/menu/productList.do?cateIdx=57&menuIdx=43" className="btn-cell">
              <img src="/20250314110653975050.png" alt="트러플안심스테이크" />
            </a>
          </li>
        </ul>
      </div>

      

      {/* 페이지네이션: 여러개의 콘텐츠를 페이지 단위로 나눠서 넘김 */}
      <div className="item-page">
        <div className="page-data">
          <ul></ul>
          <p className="line"><span></span></p>
        </div>
      </div>
    </div>
  );
}
