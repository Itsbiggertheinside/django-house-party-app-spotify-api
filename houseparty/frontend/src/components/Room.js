import React, { Component, useState, useEffect } from 'react'
import { useParams } from 'react-router-dom';



export default function Room() {

    const params = useParams();
    const [roomData, setRoomData] = useState({});

    useEffect(() => {
        getRoomDetail();
    }, []);

    const getRoomDetail = async () => {
        const response = await fetch('http://127.0.0.1:8000/api/' + params.code)
        const data = await response.json()
        setRoomData(data)
    }


    return (
        <div>
            <p>Kod: {roomData.code}</p>
            <p>Parça durdurulabilir mi? {roomData.guest_can_pause?'True':'False'}</p>
            <p>Şarkıyı geçmek için kalan oy: {roomData.votes_to_skip}</p>
            <p>Şifreli oda mı? {roomData.is_locked?'True':'False'}</p>
        </div>
    )
}
