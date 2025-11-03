// 로고 + GNB(메인메뉴) + 글로벌 메뉴
import './Header.css';


export default function Header() {
  return (
    <header id="dHead">
      <div className="inner">
        {/* 로고 */}
        <h1 className="logo">
          <a href="/"><img src="/logo_white_type_02.png" alt="OUTBACK 로고" />
          </a>
        </h1>

        {/* GNB */}
        <nav id="gnb" className="gnb-wrap">
          <ul className="gnb-list">
            <li className="gnb-01">
              <a href="/main.do?menuIdx=26">BRAND</a>
              <div className="snb">
                <div className="snb-list">
                  <h3><a href="#">BRAND</a></h3>
                  <ul>
                    <li><a href="/">OUTBACK STORY</a></li>
                    <li><a href="/">KERRR FAMILY</a></li>
                    <li><a href="/">BEEF STORY</a></li>
                    <li><a href="/">STEAK STORY</a></li>
                    <li><a href="/">OUTBACK CSR</a></li>
                  </ul>
                </div>
              </div>
            </li>

            <li className="gnb-02">
              <a href="/main.do?menuIdx=43">MENU</a>
              <div className="snb">
                <div className="snb-list">
                  <h3><a href="#">MENU</a></h3>
                  <ul>
                    <li><a href="/">BEVERAGES ＆ ALCOHOL</a></li>
                    <li><a href="/">APPETIZERS & SALADS</a></li>
                    <li><a href="/">SIZZLING BONE-IN STEAK</a></li>
                    <li><a href="/">BLACK LABEL CHEF EDDITION</a></li>
                    <li><a href="/">SPECIAL STEAKS & BACK RIBS</a></li>
                    <li><a href="/">SIDES</a></li>
                    <li><a href="/">PASTA & RICE</a></li>
                    <li><a href="/">DESSERTS</a></li>
                    <li><a href="/">WINES</a></li>
                    <li><a href="/">LUNCH SET</a></li>
                    <li><a href="/">DELIVERY</a></li>
                  </ul>
                </div>
              </div>
            </li>

            <li className="gnb-03">
              <a href="/main.do?menuIdx=28">MEMBERSHIP</a>
              <div className="snb">
                <div className="snb-list">
                  <h3><a href="#">MEMBERSHIP</a></h3>
                  <ul>
                    <li><a href="/">BOOMERANG MEMBERSHIP</a></li>
                    <li><a href="/">MEMBERSHIP BENEFIT</a></li>
                  </ul>
                </div>
              </div>
            </li>

            <li className="gnb-04">
              <a href="/main.do?menuIdx=29">BENEFIT</a>
              <div className="snb">
                <div className="snb-list">
                  <h3><a href="#">BENEFIT</a></h3>
                  <ul>
                    <li><a href="/">CREDIT CARDS</a></li>
                    <li><a href="/">SKT & KT</a></li>
                    <li><a href="/">POINT PAYMENT</a></li>
                    <li><a href="/">VOUCHER</a></li>
                  </ul>
                </div>
              </div>
            </li>

            <li className="gnb-05">
              <a href="/">STORE</a>
              <div className="snb">
                <div className="snb-list">
                  <h3><a href="#">STORE</a></h3>
                  <ul>
                    <li><a href="/">매장 찾기</a></li>
                  </ul>
                </div>
              </div>
            </li>
          </ul>
          <span className="bar"></span>
        </nav>

        {/* 글로벌 메뉴 */}
        <ul className="global-menu">
          <li><a href="/customer/inquiry.do">고객의 소리</a></li>
          <li><a href="/recruit/storeRecruitList.do?menuIdx=83">채용</a></li>
          <li><a href="#">로그인</a></li>
          <li><a href="#">회원가입</a></li>
        </ul>
      </div>
    </header>
  );
}
