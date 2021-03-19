import React, { Component } from 'react'
import { Container, Grid, TextField, Button, Typography, Paper } from '@material-ui/core'
import signupVector from '../vectors/cherry-sign-up.png'

export default class HomePage extends Component {
    render() {
        return (
            <div>
                <Container>
                    <Grid container justify="center" spacing={10}>
                        {/* <Grid item md={4}>
                            <Paper style={{ padding: '2rem' }} elevation={2}>
                                <Typography style={{ marginBottom: '2.5rem' }} variant="h3" component="h3">Giriş Yap</Typography>
                                <form noValidate autoComplete="off">
                                    <TextField style={{ marginBottom: '1rem' }} label="Kullanıcı Adı:" variant="outlined" size="small" fullWidth />
                                    <TextField style={{ marginBottom: '1rem' }} label="Kullanıcı Şifresi:" type="password" variant="outlined" size="small" fullWidth />
                                    <Button variant='outlined' color='primary' size="medium">Giriş Yap</Button>
                                </form>
                            </Paper>
                        </Grid> */}
                        <Grid item md={5} className='vector-container'>
                            <img className='vector' src={signupVector} />
                        </Grid>

                        <Grid item md={4}>
                            <Paper style={{ padding: '2rem', marginTop: '50vh', transform: 'translateY(-50%)' }} elevation={2}>
                                <Typography style={{ marginBottom: '2.5rem' }} variant="h3" component="h3">Kayıt Ol</Typography>
                                <form noValidate autoComplete="off">
                                    <TextField style={{ marginBottom: '1rem' }} label="Kullanıcı Adı:" variant="outlined" size="small" fullWidth />
                                    <TextField style={{ marginBottom: '1rem' }} label="Kullanıcı Şifresi:" type="password" variant="outlined" size="small" fullWidth />
                                    <TextField style={{ marginBottom: '1rem' }} label="Kullanıcı Şifresi (Tekrar):" type="password" variant="outlined" size="small" fullWidth />
                                    <Button variant='outlined' color='primary' size="medium">Kayıt Ol</Button>
                                </form>
                            </Paper>
                        </Grid>
                    </Grid>
                </Container>
            </div>
        )
    }
}
