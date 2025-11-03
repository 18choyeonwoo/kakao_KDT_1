import {useEffect, useRef, useState } from 'react';

export default function useInView(options= {threshold:0.15}) { //뷰포트가 0.15 이상이면 트루
    const ref = useRef(null); // dom요소를 저장할 ref
    const [inView, setInView] = useState(false); //초기값은 false(보이지 않음)
    useEffect(() => { 
        const io = new IntersectionObserver(([e]) => setInView(e.isIntersecting), options);  //setInview에 e의 상태를 전달
        //io : 가시성 변화 감지. option이 true면 이벤트시작
        if (ref.current) io.observe(ref.current); //dom관찰
        return () => io.disconnect(); //연결 해제
     }, [options] ); //option=true 일때 실행되는 useEffect

     return [ref, inView];
}