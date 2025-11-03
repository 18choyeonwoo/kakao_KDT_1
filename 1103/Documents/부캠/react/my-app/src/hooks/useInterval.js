import { useEffect, useRef } from "react";

export default function useInterval(callback, delay, paused = false){
    const savedCb = useRef(callback); //리렌더링 발생을 막음
    useEffect (() => {
        savedCb.current = callback;
    }, [callback]); //콜백이 바뀔때마다 savedCb 업데이트

    useEffect(() => {
        if (paused || delay == null) return; //일시정지이거나, delay(따로 인식 없을때) 리턴  
        const id = setInterval(()=> savedCb.current(), delay); //조건 충족시 인터벌 실행.
        return () => clearInterval(id); //정리함수, 기존 인터벌 제거
    }, [delay, paused]);
}
// setInterval을 안전하게 쓰게 해주는 훅