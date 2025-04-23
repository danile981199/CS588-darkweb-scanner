import React, { useState } from 'react';
import { Container, Typography, Box, MenuItem, Select, FormControl, InputLabel, Button, TextField, Link, Paper } from '@mui/material';
import Logo from "../assets/images/dark-web/darkweb_logo.png";


const SearchPersonalInfoPage = () => {
  const [infoType, setInfoType] = useState('');
  const [url, setUrl] = useState('');

  const handleSearch = async () => {
    try {
      const response = await fetch('http://127.0.0.1:5000/api/search-info', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ type: infoType, url }),
      });

      if (!response.ok) throw new Error('Network response was not ok');

      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(new Blob([blob]));
      const link = document.createElement('a');
      link.href = downloadUrl;
      link.setAttribute('download', `configuration.txt`);
      document.body.appendChild(link);
      link.click();
      link.parentNode.removeChild(link);

    } catch (error) {
      console.error('Error fetching the search results:', error);
      alert('An error occurred while fetching the search results.');
    }
  };

  return (
    <Container maxWidth="sm">
      <Paper elevation={3} sx={{ p: 4, my: 5, borderRadius: 2 }}>
        
        <Box sx={{ display: 'flex', justifyContent: 'center', mb: 3 }}> 
          <img src={Logo} alt="Dark Web Logo" style={{ width: 80, height: 80 }} />
        </Box>
        
        <Typography variant="h5" gutterBottom align="center" sx={{ mb: 5, fontFamily: 'Times New Roman, serif' }}>
          Search Personal Information
        </Typography>



        <TextField
          fullWidth
          label="Enter URL to scan" 
          variant="outlined"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          helperText={(
            <span>
              Example:{' '}
              <Link href="https://csectest.wordpress.com/bad-email/" target="_blank" rel="noopener">
                https://csectest.wordpress.com/bad-email/
              </Link>
            </span>
          )}
          sx={{ mb: 3, fontFamily: 'Times New Roman, serif' }}
        />

        <FormControl fullWidth variant="outlined" sx={{ mb: 3, fontFamily: 'Times New Roman, serif'  }}>
          <InputLabel id="info-type-label">Information Type</InputLabel>
          <Select
            labelId="info-type-label" 
            value={infoType}
            label="Information Type" 
            onChange={(e) => setInfoType(e.target.value)}
          >
            <MenuItem value="ssn">SSN</MenuItem>
            <MenuItem value="email">Email Address</MenuItem>
            <MenuItem value="names">Names</MenuItem>
            <MenuItem value="address">Address</MenuItem>
            <MenuItem value="NAPN">NAPN</MenuItem>
            <MenuItem value="CCD">CCD</MenuItem>
          </Select>
        </FormControl>

        <Button
          variant="contained"
          color="primary"
          fullWidth
          size="large"
          onClick={handleSearch}
          disabled={!infoType || !url}
          sx={{ py: 1.5, borderRadius: 1 }}
        >
          Search
        </Button>
      </Paper>
    </Container>
  );
};

export default SearchPersonalInfoPage;
