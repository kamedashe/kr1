import toast from 'react-hot-toast';

export const useToast = () => {
  return {
    success: (message) => toast.success(message, {
      duration: 3000,
      position: 'top-right',
      style: {
        background: '#10B981',
        color: '#fff',
      },
    }),

    error: (message) => toast.error(message, {
      duration: 4000,
      position: 'top-right',
      style: {
        background: '#EF4444',
        color: '#fff',
      },
    }),

    loading: (message) => toast.loading(message, {
      position: 'top-right',
    }),

    promise: (promise, messages) => toast.promise(promise, messages, {
      position: 'top-right',
    }),

    custom: (message, options) => toast(message, options),

    dismiss: (toastId) => toast.dismiss(toastId),
  };
};
