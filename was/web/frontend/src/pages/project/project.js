import React from 'react'
import { Carousel } from 'antd';
import { TopMenu } from '../../components/common'

// carousel 설정
const contentStyle = {
    height: '160px',
    color: '#fff',
    lineHeight: '160px',
    textAlign: 'center',
    background: '#364d79',
};

const Project = () => {
    return (
        <>
            <TopMenu/>
            <h1>Members</h1>
            {/*  본문  */}
            <Carousel autoplay>
                <div>
                    <h3 style={contentStyle}>안영훈</h3>
                </div>
                <div>
                    <h3 style={contentStyle}>김영찬</h3>
                </div>
                <div>
                    <h3 style={contentStyle}>백수연</h3>
                </div>
                <div>
                    <h3 style={contentStyle}>신재현</h3>
                </div>
            </Carousel>
            <h5 style={{textAlign:"center"}}>(마우스 올리면 멈춤)</h5>
        </>
    )
}

export default Project