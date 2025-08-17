export default function ProductCard({
  en, ko, info, linkFind, linkReserve, visual, title,
  onHoverChange,                // ⬅️ 추가
}) {
  return (
    <div className="main-product-cell">
      <div className="txt-wrap">
        {/* <img
          className="visual"
          src={visual}
          alt={title || ko || en}
          onMouseEnter={() => onHoverChange?.(true)}
          onMouseLeave={() => onHoverChange?.(false)}
        /> */}
        <p className="en-name">{en}</p>
        <p className="ko-name">{ko}</p>
        <p className="info">{info}</p>
        <p className="btns">
          <a href={linkFind} className="btn-02 type-05">매장 찾기</a>
          <a href={linkReserve} target="_blank" rel="noreferrer" className="btn-02 type-01">네이버 예약</a>
        </p>
      </div>

      {/* 배경이미지 카드(클릭 영역) */}
      <a
        href={linkReserve}
        className="visual"
        style={{ backgroundImage: `url('${visual}')` }}
        title={title ?? ko}
        onMouseEnter={() => onHoverChange?.(true)}
        onMouseLeave={() => onHoverChange?.(false)}
      >
        <span className="blind">링크 이동</span>
      </a>
    </div>
  );
}
