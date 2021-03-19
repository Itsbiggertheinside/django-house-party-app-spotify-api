import React, { Component } from 'react'
import { Link, useHistory } from 'react-router-dom';
import { Button, Grid, Typography, TextField, FormHelperText, FormControl, Radio, RadioGroup, FormControlLabel } from '@material-ui/core';
import cherryRibbon from '../vectors/cherry-ribbon.png'


export default function RoomCreatePage() {

    let history = useHistory();

    let data = {
        code: '',
        guest_can_pause: false,
        votes_to_skip: 2,
    }

    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    function handleCode(e) {
        data.code = e.target.value
    }

    function handleGuestCanPause(e) {
        data.guest_can_pause = e.target.value
    }

    function handleVotesToSkip(e) {
        data.votes_to_skip = e.target.value
    }

    function handleCreateRoomButton() {
        const requestOption = {
            method: 'POST',
            headers: {
                'X-CSRFToken': getCookie('csrftoken'),
                'Authorization': `Token ${sessionStorage.getItem('token')}`,
                'Accept': 'application/json, text/plain',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code: data.code,
                guest_can_pause: data.guest_can_pause,
                votes_to_skip: data.votes_to_skip
            })
        }

        fetch('http://127.0.0.1:8000/api/', requestOption)
        .then(response => response.json())
        .then(data => history.push('/room/' + data.code))
        .catch(err => console.log(err))
    }

    return (     
            <div className='jac'>
                <Grid container spacing={1}>
                    <Grid item xs={12} align='center'>
                        <Typography component='h4' variant='h4'>Create a Room</Typography>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <FormControl>
                            <TextField required={true} type='text' onChange={handleCode} inputProps={{min: 1, style: { textAlign: 'center' }}} />
                            <FormHelperText><div align='center'>Enter a Room Code</div></FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <FormControl component='fieldset'>
                            <RadioGroup row defaultValue='false' onChange={handleGuestCanPause}>
                                <FormControlLabel value='true' control={<Radio color='primary' />} label='Play / Pause' labelPlacement='bottom' />
                                <FormControlLabel value='false' control={<Radio color='secondary' />} label='No Control' labelPlacement='bottom' />
                            </RadioGroup>
                            <FormHelperText><div align='center'>Guest Control of Playback State</div></FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <FormControl>
                            <TextField required={true} type='number' defaultValue={2} onChange={handleVotesToSkip} inputProps={{min: 1, style: { textAlign: 'center' }}} />
                            <FormHelperText><div align='center'>Votes Required to Skip Song</div></FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <Button onClick={handleCreateRoomButton} color='primary' variant='contained'>Create a Room</Button>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <Button color='secondary' variant='contained' to='/' component={Link}>Back to Room List</Button>
                    </Grid>
                </Grid>
            </div>
    )
}



// Örnek login olma işlemi
    // componentDidMount() {

    //     const requestOption = {
    //         method: 'POSt',
    //         headers: {
    //             'Accept': 'application/json, text/plain',
    //             'Content-Type': 'application/json'
    //         },
    //         body: JSON.stringify({
    //             username: 'testuser',
    //             password: 'trtbelgesel'
    //         })
    //     }

    //     fetch('http://127.0.0.1:8000/api/rest-auth/login/', requestOption)
    //         .then(response => response.json())
    //         .then(data => {
    //           const token = data.key
    //           sessionStorage.setItem('token', token)
    //         })
    //         .catch(err => console.log(err))
    // }