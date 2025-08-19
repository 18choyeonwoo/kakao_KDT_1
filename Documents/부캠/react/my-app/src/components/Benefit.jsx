import './Benefit.css';

export default function Benefit() {
  return (
    <div className="main-benefit">
      <div className="inner-data">
        {/* 상단 이미지 */}
        <div className="benefit-top-img">
          <img
            src="/main_benefit_obj_01.jpg"
            alt="Outback Benefit Banner"
          />
        </div>
         <div className="benefit-img bg"
         style={{ backgroundImage: 'url(/main_benefit_visual.jpg)' }}
         >
        <h3 className="akrobat">OUTBACK BENEFIT
        </h3>

        <p className="info">다양한 멤버십과 제휴 할인 혜택을 누리세요</p>

        
          <div className="info-icon">
            <ul>
          <li>
            <a href="/benefit/membershipBenefit.do?menuIdx=302">
              <span className="icon">
                <img
                  src="/main_benefit_icon_01.png"
                  alt="MEMBERSHIP"
                />
              </span>
              <span className="icon-name akrobat">MEMBERSHIP</span>
              <span className="icon-info">
                부메랑클럽 가입하고
                <br />멤버십 혜택 풍성하게 즐겨보세요
              </span>
            </a>
          </li>

          <li>
            <a href="/partner/card.do?menuIdx=29">
              <span className="icon">
                <img
                  src="/main_benefit_icon_02.png"
                  alt="DISCOUNT"
                />
              </span>
              <span className="icon-name akrobat">DISCOUNT</span>
              <span className="icon-info">
                아웃백 제휴 할인 혜택의
                <br />기회를 놓치지 마세요
              </span>
            </a>
          </li>

          <li>
            <a href="/partner/gift02.do?menuIdx=54">
              <span className="icon">
                <img
                  src="/main_benefit_icon_03.png"
                  alt="GIFT CARD"
                />
              </span>
              <span className="icon-name akrobat">GIFT CARD</span>
              <span className="icon-info">
                소중한 사람에게
                <br />감사한 마음을 선물하세요
              </span>
            </a>
          </li>
          </ul>
          </div>
        </div>
      </div>
    </div>
  );
}
