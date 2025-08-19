// src/components/MainProduct.jsx
import { useCallback, useEffect, useMemo, useState } from "react";
import useInView from "../hooks/useInView";
import useInterval from "../hooks/useInterval";
import ProductCard from "./ProductCard";
import './MainProduct.css';


export default function MainProduct() {
  const items = [
    {
      en: "GARLIC\nRIBEYE",
      ko: "갈릭 립아이",
      info: "구운 마늘과 마늘칩이 어우러진 \n꽃등심 스테이크",
      visual: "/20240717154449016372.jpg",
      title: "갈릭 립아이",
    },
    {
      en: "GOLD COAST \nCOCONUT \nSHRIMP",
      ko: "골드 코스트 코코넛 쉬림프",
      info: "달콤하고 고소한 코코넛 가루를 묻혀 \n바삭하게 튀긴 새우 요리",
      visual: "/20190108172841884005.jpg",
      title: "골드 코스트 코코넛 슈림프",
    },
    {
      en: "BABY BACK \nRIBS",
      ko: "베이비 백 립",
      info: "부드러운 돼지갈비에 아웃백만의 특제 소스를 \n발라 구워낸 바비큐 요리",
      visual: "/20180627183554751017.jpg",
      title: "갈릭 립아이",
    },
    {
      en: "AUSSIE \nCHEESE \nFRIES",
      ko: "오지 치즈 후라이즈",
      info: "두툼한 감자튀김에 체다치즈, 잭치즈를 듬뿍 \n녹여 베이컨을 뿌린 메뉴",
      visual: "/20180627183609110019.jpg",
      title: "갈릭 립아이",
    },
  ];

  const len = items.length; //슬라이드 개수
  const [sectionRef, inView] = useInView({ threshold: 0.15 });
  // dom에 꽂을 ref & 15% 이상 보이는지 나타내는 불린값 inview(true여야만 동작)
  const [idx, setIdx] = useState(0); //슬라이스 인덱스(0부터)
  const [paused, setPaused] = useState(false); //자동재생 일시정지 여부

  const next = useCallback(() => setIdx(i => (i + 1) % len), [len]); //다음슬라이드로
  const prev = useCallback(() => setIdx(i => (i - 1 + len) % len), [len]); //이전슬라이드로

  // 섹션이 보일 때만 자동 슬라이드 (호버 시 일시정지)
  useInterval(next, 4000, paused || !inView);
  //4초마다 next 실행, 뒤에는 인터벌 정지 조건

  // 키보드 좌/우
  // useEffect(() => {
  //   const onKey = (e) => { 키보드 이벤트가 발생할때 호출되는 함수
  //     if (e.key === "ArrowRight") next(); 오른쪽 화살표면 다음 슬라이드
  //     if (e.key === "ArrowLeft") prev() 
  //   };
  //   window.addEventListener("keydown", onKey); 전역(윈도우) 에 키다운 리스너 붙임
  //   return () => window.removeEventListener("keydown", onKey); 이펙트 정리
  // }, [next, prev]); 의존성(다음/이전) 바뀔때마다 실행

  // 프리로드(다음 카드 비동기 로딩)
  useEffect(() => {
    const preload = new Image();
    preload.src = items[(idx) % len].visual;
  }, [idx, len, items]);

  const dots = useMemo(() => Array.from({ length: len }), [len]); //계산결과 메모
  const cur = items[(idx+1) % len]; //현재 표시중인데이터
  const nxt = items[(idx) % len] //미리보기 데이터

  return (
    <section
      ref={sectionRef} //io로 관찰할 dom. 이섹션이 뷰포트 15%이상 보이면 true 
      id="dBody"
      className={`main main-product-section ${inView ? "enter" : ""}`}
      // 보이면, css에서 enter을 사용해서 디자인

      aria-roledescription="carousel" //접근성 개선하는 코드
    >
      <div className="main-product">
        <div className="side-data-wrap">
          <div className="slide-data">

            {/* 다음 카드 미리보기 */}
            <div className={`side-cell fade ${inView ? "on" : ""}`}>
              <div
                className="visual"
                style={{ backgroundImage: `url(${nxt.visual})` }}
              />
            </div>

            {/* 현재 큰 카드 */}
            <div className={`slide-cell fade ${inView ? "on" : ""}`}>

              <div className="main-card">

                {/* 설명 컨테이너 */}
                <div className="main-text">
                  <p className="en-name">{cur.en}</p>
                  <p className="ko-name">{cur.ko}</p>
                  <p className="info">{cur.info}</p>
                </div>

                {/* 사진 컨테이너 */}
                <div className="main-visual">
                  <img src={cur.visual} alt={cur.en} className="main-visual-img" />
                </div>

              </div>
            </div>

          </div>
        </div>

        {/* 좌/우 네비게이션 */}
        <button className="mp-nav prev" aria-label="이전" onClick={prev}>‹</button>
        <button className="mp-nav next" aria-label="다음" onClick={next}>›</button>

        {/* 점 네비 */}
        <div className="mp-dots" role="tablist" aria-label="슬라이드 선택">
          {dots.map((_, i) => (
            <button
              key={i}
              role="tab"
              aria-selected={i === idx}
              className={`mp-dot ${i === idx ? "is-active" : ""}`}
              onClick={() => setIdx(i)}
            />
          ))}
        </div>
      </div>
    </section>
  );
}