import React, { Component } from 'react'
import { Link } from 'react-router-dom';
import { Button, Grid, Typography, TextField, FormHelperText, FormControl, Radio, RadioGroup, FormControlLabel } from '@material-ui/core';



export default class RoomCreatePage extends Component {

    render() {

        const data = {
            code: '',
            guest_can_pause: false,
            votes_to_skip: 1,
        }

        return (            
            <div>
                <Grid container spacing={1}>
                    <Grid item xs={12} align='center'><Typography component='h4' variant='h4'>Create a Room</Typography></Grid>
                    <Grid item xs={12} align='center'>
                        <FormControl>
                            <TextField required={true} type='text' defaultValue={data.code} onChange={e => data.code = e.target.value} inputProps={{min: 1, style: { textAlign: 'center' }}} />
                            <FormHelperText><div align='center'>Enter a Room Code</div></FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <FormControl component='fieldset'>
                            <RadioGroup row defaultValue={data.guest_can_pause} onChange={e => data.guest_can_pause = e.target.value}>
                                <FormControlLabel value='true' control={<Radio color='primary' />} label='Play / Pause' labelPlacement='bottom' />
                                <FormControlLabel value='false' control={<Radio color='secondary' />} label='No Control' labelPlacement='bottom' />
                            </RadioGroup>
                            <FormHelperText><div align='center'>Guest Control of Playback State</div></FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <FormControl>
                            <TextField required={true} type='number' defaultValue={data.votes_to_skip} onChange={e => data.votes_to_skip = e.target.value} inputProps={{min: 1, style: { textAlign: 'center' }}} />
                            <FormHelperText><div align='center'>Votes Required to Skip Song</div></FormHelperText>
                        </FormControl>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <Button onClick={console.log(data)} color='primary' variant='contained'>Create a Room</Button>
                    </Grid>
                    <Grid item xs={12} align='center'>
                        <Button color='secondary' variant='contained' to='/' component={Link}>Back to Room List</Button>
                    </Grid>
                </Grid>
            </div>
        )
    }
}
