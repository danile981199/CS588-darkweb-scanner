import React, { useEffect, useState } from 'react';
import { Container, Typography, Box, Paper, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const ResultPage = () => {
  const [resultData, setResultData] = useState(null);
  const navigate = useNavigate();

  useEffect(() => {
    const storedResult = localStorage.getItem('lastResult');
    if (storedResult) {
      setResultData(JSON.parse(storedResult));
    }
  }, []);

  return (
    <Container maxWidth="md">
      <Paper sx={{ p: 4, mt: 5, borderRadius: 2 }}>
        <Typography variant="h5" gutterBottom>
          Scan Results
        </Typography>

        {resultData ? (
          <>
            <Typography variant="subtitle1" sx={{ mb: 2 }}>
              <strong>URL:</strong> {resultData.url}<br />
              <strong>Type:</strong> {resultData.type}
            </Typography>

            <Box
              sx={{
                maxHeight: 400,
                overflowY: 'auto',
                whiteSpace: 'pre-wrap',
                backgroundColor: '#f5f5f5',
                p: 2,
                borderRadius: 1,
                mb: 3
              }}
            >
              {resultData.results.map((line, idx) => (
                <Typography key={idx} variant="body2">• {line}</Typography>
              ))}
            </Box>

            <Typography variant="h6" gutterBottom>
              Configuration File
            </Typography>
            <Box
              sx={{
                maxHeight: 300,
                overflowY: 'auto',
                whiteSpace: 'pre-wrap',
                backgroundColor: '#eeeeee',
                p: 2,
                borderRadius: 1
              }}
            >
              <Typography variant="body2">
                {resultData.config}
              </Typography>
            </Box>
          </>
        ) : (
          <Typography sx={{ mt: 2 }}>
            No result available. Please run a search first.
          </Typography>
        )}

        <Button
          variant="contained"
          sx={{ mt: 3 }}
          onClick={() => navigate('/search-personal-info')}
        >
          Back to Search
        </Button>
      </Paper>
    </Container>
  );
};

export default ResultPage;
