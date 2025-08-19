import styles from './MainReward.module.css';

export default function MainReward() {
  return (
    <div className={styles['main-reward']}>
      <div className={styles['inner-data']}>
        <div className={styles['reward-title']}>
          <div className={styles['txt-data']}>
            <h3 className="akrobat">
              BOOMERANG <em>REWARD</em>
            </h3>
            <p className={styles.info}>
              부메랑 카드<br />리워드 혜택을 만나보세요
            </p>
            <p className={styles['btn-more']}>
              <a href="/benefit/membershipBenefit.do?menuIdx=302">자세히 보기</a>
            </p>
          </div>
          <div className={styles.line}>
            <span></span><span></span><span></span><span></span>
          </div>
        </div>

        <ol className={styles.list}>
          <li className={styles.item}>
            <em>01</em>
            <p className={styles['reward-name']}>본-인 스테이크 쿠폰</p>
            <p className={styles['reward-info']}>
              본-인 스테이크 한정<br />1만원 할인 혜택 제공
            </p>
          </li>
          <li className={styles.item}>
            <em>02</em>
            <p className={styles['reward-name']}>연 1회, 부메랑 쿠폰</p>
            <p className={styles['reward-info']}>
              부메랑 회원이라면 누구나<br />1만원 할인 혜택 제공
            </p>
          </li>
          <li className={styles.item}>
            <em>03</em>
            <p className={styles['reward-name']}>와인 콜키지 1만원</p>
            <p className={styles['reward-info']}>
              와인 콜키지를 1만원에<br />즐길 수 있는 혜택 제공
            </p>
          </li>
          <li className={styles.item}>
            <em>04</em>
            <p className={styles['reward-name']}>와인 2잔 9,000원</p>
            <p className={styles['reward-info']}>
              와인 2잔을 9,000원에<br />즐길 수 있는 혜택 제공
            </p>
          </li>
          <li className={styles.item}>
            <em>05</em>
            <p className={styles['reward-name']}>10% 할인 또는 최대 3% 적립</p>
            <p className={styles['reward-info']}>
              멤버십 바코드만 있다면<br />상시 10% 할인 또는 최대 3% 적립!
            </p>
          </li>
          <li className={styles.item}>
            <em>06</em>
            <p className={styles['reward-name']}>부메랑 포인트</p>
            <p className={styles['reward-info']}>
              3,000P 이상 보유 시,<br />10P 단위로 현금처럼 사용 가능
            </p>
          </li>
        </ol>
      </div>
      <p className={styles['obj-01']}></p>
    </div>
  );
}
